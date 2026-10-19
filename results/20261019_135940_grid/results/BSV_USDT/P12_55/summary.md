# EMA Hourly Continuation — BSV/USDT P12_55

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1138 |
| net_profit_factor | 0.4299 |
| net_win_rate | 0.4227 |
| gross_profit_factor | 0.7959 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -8.8906 |
| sortino_ratio | -4.2121 |
| max_drawdown | 0.9950 |
| cagr | -0.8768 |
| net_avg_win | 15.5947 |
| net_avg_loss | -26.5586 |
| avg_hold_time_bars | 7.2337 |
| exposure | 0.3742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
