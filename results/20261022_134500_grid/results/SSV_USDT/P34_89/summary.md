# EMA Hourly Continuation — SSV/USDT P34_89

**Symbol:** SSV/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.5331 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.8243 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -5.4224 |
| sortino_ratio | -2.0546 |
| max_drawdown | 0.9204 |
| cagr | -0.6255 |
| net_avg_win | 32.6891 |
| net_avg_loss | -48.5667 |
| avg_hold_time_bars | 8.3135 |
| exposure | 0.2724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
