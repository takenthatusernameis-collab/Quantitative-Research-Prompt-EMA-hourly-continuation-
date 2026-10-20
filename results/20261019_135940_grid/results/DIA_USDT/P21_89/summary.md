# EMA Hourly Continuation — DIA/USDT P21_89

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.6127 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.9378 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -4.4314 |
| sortino_ratio | -1.6297 |
| max_drawdown | 0.8749 |
| cagr | -0.5444 |
| net_avg_win | 42.4921 |
| net_avg_loss | -59.8486 |
| avg_hold_time_bars | 12.0837 |
| exposure | 0.3789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
