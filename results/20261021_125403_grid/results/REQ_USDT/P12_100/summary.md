# EMA Hourly Continuation — REQ/USDT P12_100

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6495 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8871 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -3.6997 |
| sortino_ratio | -1.2417 |
| max_drawdown | 0.7704 |
| cagr | -0.4374 |
| net_avg_win | 55.3077 |
| net_avg_loss | -72.4243 |
| avg_hold_time_bars | 19.9856 |
| exposure | 0.5060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
