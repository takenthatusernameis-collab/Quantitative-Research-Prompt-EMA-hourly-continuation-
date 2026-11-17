# EMA Hourly Continuation — NUM/USDT P20_34

**Symbol:** NUM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.2975 |
| net_win_rate | 0.3290 |
| gross_profit_factor | 0.7524 |
| gross_win_rate | 0.3614 |
| sharpe_ratio | -13.1692 |
| sortino_ratio | -6.1970 |
| max_drawdown | 0.9997 |
| cagr | -0.9590 |
| net_avg_win | 11.9248 |
| net_avg_loss | -19.6547 |
| avg_hold_time_bars | 3.6191 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
