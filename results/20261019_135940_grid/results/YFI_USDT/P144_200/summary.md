# EMA Hourly Continuation — YFI/USDT P144_200

**Symbol:** YFI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.2820 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.6778 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -6.3231 |
| sortino_ratio | -1.9418 |
| max_drawdown | 0.9166 |
| cagr | -0.6162 |
| net_avg_win | 17.7940 |
| net_avg_loss | -48.7831 |
| avg_hold_time_bars | 4.8655 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
