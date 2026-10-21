# EMA Hourly Continuation — TAO/USDT P34_89

**Symbol:** TAO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.9001 |
| net_win_rate | 0.5236 |
| gross_profit_factor | 1.0929 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -0.6226 |
| sortino_ratio | -0.1753 |
| max_drawdown | 0.2365 |
| cagr | -0.0812 |
| net_avg_win | 86.2613 |
| net_avg_loss | -105.3130 |
| avg_hold_time_bars | 11.7932 |
| exposure | 0.2048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
