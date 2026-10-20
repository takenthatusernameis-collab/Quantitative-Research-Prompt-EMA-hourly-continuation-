# EMA Hourly Continuation — GTC/USDT P55_200

**Symbol:** GTC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.5881 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8036 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -3.0768 |
| sortino_ratio | -0.8608 |
| max_drawdown | 0.6466 |
| cagr | -0.3301 |
| net_avg_win | 51.7406 |
| net_avg_loss | -71.2849 |
| avg_hold_time_bars | 21.3708 |
| exposure | 0.3798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
