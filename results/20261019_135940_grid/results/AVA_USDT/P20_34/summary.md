# EMA Hourly Continuation — AVA/USDT P20_34

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1072 |
| net_profit_factor | 0.2843 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.7209 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -10.7876 |
| sortino_ratio | -5.0162 |
| max_drawdown | 0.9985 |
| cagr | -0.9244 |
| net_avg_win | 8.9118 |
| net_avg_loss | -22.2496 |
| avg_hold_time_bars | 2.8573 |
| exposure | 0.1392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
