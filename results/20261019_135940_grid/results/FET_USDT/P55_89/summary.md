# EMA Hourly Continuation — FET/USDT P55_89

**Symbol:** FET/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.5088 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 0.8599 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -5.4465 |
| sortino_ratio | -1.9260 |
| max_drawdown | 0.9137 |
| cagr | -0.6149 |
| net_avg_win | 32.1406 |
| net_avg_loss | -53.3340 |
| avg_hold_time_bars | 4.4672 |
| exposure | 0.1300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
