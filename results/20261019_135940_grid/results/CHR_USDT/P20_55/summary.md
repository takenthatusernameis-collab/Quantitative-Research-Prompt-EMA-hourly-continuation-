# EMA Hourly Continuation — CHR/USDT P20_55

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.5321 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.8875 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -6.4013 |
| sortino_ratio | -2.7799 |
| max_drawdown | 0.9670 |
| cagr | -0.7376 |
| net_avg_win | 25.9690 |
| net_avg_loss | -38.8751 |
| avg_hold_time_bars | 5.8952 |
| exposure | 0.2545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
