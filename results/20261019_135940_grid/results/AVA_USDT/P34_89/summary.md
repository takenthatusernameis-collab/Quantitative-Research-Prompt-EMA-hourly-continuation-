# EMA Hourly Continuation — AVA/USDT P34_89

**Symbol:** AVA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.5898 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0042 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -3.8916 |
| sortino_ratio | -1.4600 |
| max_drawdown | 0.8397 |
| cagr | -0.5090 |
| net_avg_win | 33.0686 |
| net_avg_loss | -57.4927 |
| avg_hold_time_bars | 6.7189 |
| exposure | 0.2184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
