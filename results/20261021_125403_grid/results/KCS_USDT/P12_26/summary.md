# EMA Hourly Continuation — KCS/USDT P12_26

**Symbol:** KCS/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.3684 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.7597 |
| gross_win_rate | 0.4217 |
| sharpe_ratio | -6.1850 |
| sortino_ratio | -1.8332 |
| max_drawdown | 0.8903 |
| cagr | -0.5788 |
| net_avg_win | 30.0478 |
| net_avg_loss | -57.7293 |
| avg_hold_time_bars | 7.3229 |
| exposure | 0.1381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
