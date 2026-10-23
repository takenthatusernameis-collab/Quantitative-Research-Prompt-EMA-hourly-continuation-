# EMA Hourly Continuation — CTC/USDT P21_55

**Symbol:** CTC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 918 |
| net_profit_factor | 0.4514 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.8691 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -7.2767 |
| sortino_ratio | -3.1014 |
| max_drawdown | 0.9803 |
| cagr | -0.7857 |
| net_avg_win | 19.6512 |
| net_avg_loss | -35.1342 |
| avg_hold_time_bars | 6.3606 |
| exposure | 0.2654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
