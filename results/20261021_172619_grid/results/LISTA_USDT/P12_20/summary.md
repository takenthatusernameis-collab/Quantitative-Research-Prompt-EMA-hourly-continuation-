# EMA Hourly Continuation — LISTA/USDT P12_20

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.6467 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9010 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -3.0756 |
| sortino_ratio | -0.9570 |
| max_drawdown | 0.6670 |
| cagr | -0.3554 |
| net_avg_win | 56.4421 |
| net_avg_loss | -77.9084 |
| avg_hold_time_bars | 5.7143 |
| exposure | 0.1232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
