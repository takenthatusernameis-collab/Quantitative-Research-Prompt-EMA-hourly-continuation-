# EMA Hourly Continuation — BTC/USDT P50_144

**Symbol:** BTC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.4831 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 1.1145 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -5.0393 |
| sortino_ratio | -1.4506 |
| max_drawdown | 0.8809 |
| cagr | -0.5232 |
| net_avg_win | 37.0082 |
| net_avg_loss | -66.4382 |
| avg_hold_time_bars | 13.7259 |
| exposure | 0.2624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
