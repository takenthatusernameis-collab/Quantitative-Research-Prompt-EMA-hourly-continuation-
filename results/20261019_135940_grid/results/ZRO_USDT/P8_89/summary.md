# EMA Hourly Continuation — ZRO/USDT P8_89

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.6836 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9326 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.2613 |
| sortino_ratio | -1.2479 |
| max_drawdown | 0.7645 |
| cagr | -0.4490 |
| net_avg_win | 49.1790 |
| net_avg_loss | -66.8701 |
| avg_hold_time_bars | 18.5693 |
| exposure | 0.6226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
