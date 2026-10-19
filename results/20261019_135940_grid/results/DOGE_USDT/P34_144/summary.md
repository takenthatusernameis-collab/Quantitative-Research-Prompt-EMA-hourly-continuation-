# EMA Hourly Continuation — DOGE/USDT P34_144

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.4988 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.8052 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -4.5197 |
| sortino_ratio | -1.3646 |
| max_drawdown | 0.8223 |
| cagr | -0.4853 |
| net_avg_win | 39.3907 |
| net_avg_loss | -62.5030 |
| avg_hold_time_bars | 18.5366 |
| exposure | 0.3910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
