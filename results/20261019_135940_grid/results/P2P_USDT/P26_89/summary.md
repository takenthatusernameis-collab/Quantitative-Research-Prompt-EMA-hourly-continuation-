# EMA Hourly Continuation — P2P/USDT P26_89

**Symbol:** P2P/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.4871 |
| net_win_rate | 0.3952 |
| gross_profit_factor | 0.6632 |
| gross_win_rate | 0.3997 |
| sharpe_ratio | -5.4452 |
| sortino_ratio | -1.9628 |
| max_drawdown | 0.9059 |
| cagr | -0.6072 |
| net_avg_win | 32.7796 |
| net_avg_loss | -43.9689 |
| avg_hold_time_bars | 10.4902 |
| exposure | 0.3161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
