# EMA Hourly Continuation — BDX/USDT P21_144

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.5215 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.8128 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -4.5755 |
| sortino_ratio | -1.3947 |
| max_drawdown | 0.8159 |
| cagr | -0.4780 |
| net_avg_win | 44.0563 |
| net_avg_loss | -65.4187 |
| avg_hold_time_bars | 15.7785 |
| exposure | 0.3270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
