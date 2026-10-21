# EMA Hourly Continuation — SUN/USDT P12_144

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.5826 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8697 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -3.3161 |
| sortino_ratio | -0.8583 |
| max_drawdown | 0.6390 |
| cagr | -0.3322 |
| net_avg_win | 59.4357 |
| net_avg_loss | -83.6258 |
| avg_hold_time_bars | 45.0811 |
| exposure | 0.6793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
