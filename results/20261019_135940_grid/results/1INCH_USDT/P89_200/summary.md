# EMA Hourly Continuation — 1INCH/USDT P89_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5998 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 1.0223 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -3.7910 |
| sortino_ratio | -1.0553 |
| max_drawdown | 0.7506 |
| cagr | -0.4100 |
| net_avg_win | 57.6038 |
| net_avg_loss | -87.7716 |
| avg_hold_time_bars | 11.3175 |
| exposure | 0.2058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
