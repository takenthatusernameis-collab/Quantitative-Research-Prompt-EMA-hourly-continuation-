# EMA Hourly Continuation — OP/USDT P55_89

**Symbol:** OP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7800 |
| net_win_rate | 0.5095 |
| gross_profit_factor | 1.0418 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -1.4019 |
| sortino_ratio | -0.3583 |
| max_drawdown | 0.3579 |
| cagr | -0.1522 |
| net_avg_win | 74.7668 |
| net_avg_loss | -99.5591 |
| avg_hold_time_bars | 5.9177 |
| exposure | 0.0850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
