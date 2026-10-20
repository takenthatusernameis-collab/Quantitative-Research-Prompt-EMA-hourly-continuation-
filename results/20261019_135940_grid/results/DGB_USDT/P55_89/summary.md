# EMA Hourly Continuation — DGB/USDT P55_89

**Symbol:** DGB/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 783 |
| net_profit_factor | 0.4115 |
| net_win_rate | 0.4074 |
| gross_profit_factor | 0.8633 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -8.4174 |
| sortino_ratio | -3.3402 |
| max_drawdown | 0.9854 |
| cagr | -0.8129 |
| net_avg_win | 21.5930 |
| net_avg_loss | -36.0769 |
| avg_hold_time_bars | 3.5364 |
| exposure | 0.1259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
