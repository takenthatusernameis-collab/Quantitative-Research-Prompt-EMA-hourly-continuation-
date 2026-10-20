# EMA Hourly Continuation — XPR/USDT P12_144

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.5280 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8196 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -4.9949 |
| sortino_ratio | -1.7130 |
| max_drawdown | 0.8937 |
| cagr | -0.5722 |
| net_avg_win | 36.3842 |
| net_avg_loss | -55.9109 |
| avg_hold_time_bars | 21.5554 |
| exposure | 0.5928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
