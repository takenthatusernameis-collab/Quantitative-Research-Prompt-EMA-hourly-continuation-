# EMA Hourly Continuation — STRAX/USDT P8_89

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.6890 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8994 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -3.5113 |
| sortino_ratio | -1.2762 |
| max_drawdown | 0.7805 |
| cagr | -0.4462 |
| net_avg_win | 56.7562 |
| net_avg_loss | -70.4447 |
| avg_hold_time_bars | 18.7534 |
| exposure | 0.5599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
