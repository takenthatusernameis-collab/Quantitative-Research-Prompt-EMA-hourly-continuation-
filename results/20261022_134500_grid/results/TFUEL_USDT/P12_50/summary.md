# EMA Hourly Continuation — TFUEL/USDT P12_50

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1290 |
| net_profit_factor | 0.4558 |
| net_win_rate | 0.3961 |
| gross_profit_factor | 0.7674 |
| gross_win_rate | 0.4101 |
| sharpe_ratio | -10.6588 |
| sortino_ratio | -5.3500 |
| max_drawdown | 0.9989 |
| cagr | -0.9317 |
| net_avg_win | 16.3743 |
| net_avg_loss | -23.5633 |
| avg_hold_time_bars | 5.7783 |
| exposure | 0.3373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
