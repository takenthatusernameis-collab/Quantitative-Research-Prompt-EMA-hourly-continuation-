# EMA Hourly Continuation — ETHFI/USDT P20_200

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7785 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9743 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -1.6239 |
| sortino_ratio | -0.4227 |
| max_drawdown | 0.4286 |
| cagr | -0.1805 |
| net_avg_win | 84.3130 |
| net_avg_loss | -101.4986 |
| avg_hold_time_bars | 43.9646 |
| exposure | 0.6775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
