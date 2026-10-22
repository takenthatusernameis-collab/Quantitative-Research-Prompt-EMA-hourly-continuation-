# EMA Hourly Continuation — ADA/USDT P12_20

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1489 |
| net_profit_factor | 0.2139 |
| net_win_rate | 0.3788 |
| gross_profit_factor | 0.8325 |
| gross_win_rate | 0.4191 |
| sharpe_ratio | -15.5354 |
| sortino_ratio | -8.6552 |
| max_drawdown | 1.0000 |
| cagr | -0.9900 |
| net_avg_win | 4.8237 |
| net_avg_loss | -13.7518 |
| avg_hold_time_bars | 1.9295 |
| exposure | 0.1306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
