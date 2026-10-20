# EMA Hourly Continuation — ZEN/USDT P8_89

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.5801 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.8649 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -4.4824 |
| sortino_ratio | -1.7278 |
| max_drawdown | 0.8780 |
| cagr | -0.5658 |
| net_avg_win | 34.9195 |
| net_avg_loss | -50.9433 |
| avg_hold_time_bars | 18.6196 |
| exposure | 0.6407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
