# EMA Hourly Continuation — RIO/USDT P8_89

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 944 |
| net_profit_factor | 0.6283 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8342 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -5.0136 |
| sortino_ratio | -2.1636 |
| max_drawdown | 0.9274 |
| cagr | -0.6470 |
| net_avg_win | 37.1422 |
| net_avg_loss | -47.5829 |
| avg_hold_time_bars | 13.4174 |
| exposure | 0.5815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
