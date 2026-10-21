# EMA Hourly Continuation — MOG/USDT P8_12

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.6781 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.8660 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -1.9177 |
| sortino_ratio | -0.4301 |
| max_drawdown | 0.3696 |
| cagr | -0.1790 |
| net_avg_win | 72.3990 |
| net_avg_loss | -93.5294 |
| avg_hold_time_bars | 5.9471 |
| exposure | 0.0671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
