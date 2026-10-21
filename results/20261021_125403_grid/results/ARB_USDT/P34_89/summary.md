# EMA Hourly Continuation — ARB/USDT P34_89

**Symbol:** ARB/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.8301 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0638 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.1764 |
| sortino_ratio | -0.3485 |
| max_drawdown | 0.3917 |
| cagr | -0.1497 |
| net_avg_win | 74.5969 |
| net_avg_loss | -96.0049 |
| avg_hold_time_bars | 12.8255 |
| exposure | 0.2472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
