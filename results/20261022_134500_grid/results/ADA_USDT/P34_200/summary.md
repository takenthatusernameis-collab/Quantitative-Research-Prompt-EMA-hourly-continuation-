# EMA Hourly Continuation — ADA/USDT P34_200

**Symbol:** ADA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6224 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 1.0102 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -2.8756 |
| sortino_ratio | -0.8077 |
| max_drawdown | 0.6392 |
| cagr | -0.3236 |
| net_avg_win | 52.8686 |
| net_avg_loss | -80.4061 |
| avg_hold_time_bars | 25.4115 |
| exposure | 0.4632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
