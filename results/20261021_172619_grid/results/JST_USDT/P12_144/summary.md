# EMA Hourly Continuation — JST/USDT P12_144

**Symbol:** JST/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7669 |
| net_win_rate | 0.5271 |
| gross_profit_factor | 1.1040 |
| gross_win_rate | 0.5301 |
| sharpe_ratio | -1.3603 |
| sortino_ratio | -0.3534 |
| max_drawdown | 0.3783 |
| cagr | -0.1523 |
| net_avg_win | 64.0810 |
| net_avg_loss | -93.1353 |
| avg_hold_time_bars | 45.7470 |
| exposure | 0.6873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
