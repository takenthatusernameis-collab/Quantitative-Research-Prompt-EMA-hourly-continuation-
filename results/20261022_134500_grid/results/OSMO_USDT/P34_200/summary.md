# EMA Hourly Continuation — OSMO/USDT P34_200

**Symbol:** OSMO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7268 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0277 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -1.9114 |
| sortino_ratio | -0.5133 |
| max_drawdown | 0.4725 |
| cagr | -0.2190 |
| net_avg_win | 67.6057 |
| net_avg_loss | -93.0160 |
| avg_hold_time_bars | 30.9258 |
| exposure | 0.5117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
