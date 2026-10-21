# EMA Hourly Continuation — HTX/USDT P144_200

**Symbol:** HTX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.3905 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.7793 |
| gross_win_rate | 0.4254 |
| sharpe_ratio | -4.4285 |
| sortino_ratio | -0.9732 |
| max_drawdown | 0.6858 |
| cagr | -0.3622 |
| net_avg_win | 45.2807 |
| net_avg_loss | -84.3242 |
| avg_hold_time_bars | 7.5175 |
| exposure | 0.0776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
