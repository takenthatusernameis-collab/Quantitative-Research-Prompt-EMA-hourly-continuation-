# EMA Hourly Continuation — BTC/USDT P20_144

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.4885 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 1.0246 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -5.0157 |
| sortino_ratio | -1.4739 |
| max_drawdown | 0.8866 |
| cagr | -0.5310 |
| net_avg_win | 36.1117 |
| net_avg_loss | -62.9009 |
| avg_hold_time_bars | 26.5344 |
| exposure | 0.5402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
