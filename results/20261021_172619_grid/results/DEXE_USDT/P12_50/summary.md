# EMA Hourly Continuation — DEXE/USDT P12_50

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.7696 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 0.9949 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.7759 |
| sortino_ratio | -0.6165 |
| max_drawdown | 0.5298 |
| cagr | -0.2475 |
| net_avg_win | 57.5727 |
| net_avg_loss | -76.3603 |
| avg_hold_time_bars | 15.0171 |
| exposure | 0.4000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
