# EMA Hourly Continuation — CTC/USDT P21_26

**Symbol:** CTC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1164 |
| net_profit_factor | 0.1677 |
| net_win_rate | 0.3514 |
| gross_profit_factor | 0.7196 |
| gross_win_rate | 0.4227 |
| sharpe_ratio | -14.9675 |
| sortino_ratio | -7.5137 |
| max_drawdown | 1.0000 |
| cagr | -0.9825 |
| net_avg_win | 4.9277 |
| net_avg_loss | -15.9139 |
| avg_hold_time_bars | 2.4734 |
| exposure | 0.1309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
