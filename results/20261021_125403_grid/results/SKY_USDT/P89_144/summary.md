# EMA Hourly Continuation — SKY/USDT P89_144

**Symbol:** SKY/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.8223 |
| net_win_rate | 0.5439 |
| gross_profit_factor | 1.1906 |
| gross_win_rate | 0.5439 |
| sharpe_ratio | -1.0469 |
| sortino_ratio | -0.2597 |
| max_drawdown | 0.3301 |
| cagr | -0.1124 |
| net_avg_win | 77.1170 |
| net_avg_loss | -111.8462 |
| avg_hold_time_bars | 7.2385 |
| exposure | 0.0965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
