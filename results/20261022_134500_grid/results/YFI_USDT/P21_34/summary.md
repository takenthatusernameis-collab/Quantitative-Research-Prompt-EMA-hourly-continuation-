# EMA Hourly Continuation — YFI/USDT P21_34

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1281 |
| net_profit_factor | 0.2814 |
| net_win_rate | 0.3794 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4301 |
| sharpe_ratio | -14.1205 |
| sortino_ratio | -7.3112 |
| max_drawdown | 0.9999 |
| cagr | -0.9783 |
| net_avg_win | 8.0562 |
| net_avg_loss | -17.5028 |
| avg_hold_time_bars | 2.7260 |
| exposure | 0.1580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
