# EMA Hourly Continuation — AEVO/USDT P144_200

**Symbol:** AEVO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.4852 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.7915 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -4.5010 |
| sortino_ratio | -1.2853 |
| max_drawdown | 0.8006 |
| cagr | -0.4675 |
| net_avg_win | 40.9961 |
| net_avg_loss | -66.6487 |
| avg_hold_time_bars | 5.3205 |
| exposure | 0.0999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
