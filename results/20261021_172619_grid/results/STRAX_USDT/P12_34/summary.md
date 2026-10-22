# EMA Hourly Continuation — STRAX/USDT P12_34

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.7886 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -4.8809 |
| sortino_ratio | -1.8941 |
| max_drawdown | 0.8877 |
| cagr | -0.5817 |
| net_avg_win | 31.9952 |
| net_avg_loss | -48.4350 |
| avg_hold_time_bars | 7.5639 |
| exposure | 0.2545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
