# EMA Hourly Continuation — EWT/USDT P50_144

**Symbol:** EWT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.4622 |
| net_win_rate | 0.4132 |
| gross_profit_factor | 0.6999 |
| gross_win_rate | 0.4192 |
| sharpe_ratio | -5.0437 |
| sortino_ratio | -1.5899 |
| max_drawdown | 0.8625 |
| cagr | -0.5334 |
| net_avg_win | 35.3978 |
| net_avg_loss | -53.9213 |
| avg_hold_time_bars | 10.0120 |
| exposure | 0.2280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
