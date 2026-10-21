# EMA Hourly Continuation — CRV/USDT P21_144

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.8431 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 1.0163 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.2195 |
| sortino_ratio | -0.3442 |
| max_drawdown | 0.4455 |
| cagr | -0.1479 |
| net_avg_win | 91.6355 |
| net_avg_loss | -108.1356 |
| avg_hold_time_bars | 27.0771 |
| exposure | 0.4788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
