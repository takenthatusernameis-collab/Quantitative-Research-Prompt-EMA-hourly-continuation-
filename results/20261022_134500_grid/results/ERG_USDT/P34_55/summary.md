# EMA Hourly Continuation — ERG/USDT P34_55

**Symbol:** ERG/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 905 |
| net_profit_factor | 0.1937 |
| net_win_rate | 0.3282 |
| gross_profit_factor | 0.3968 |
| gross_win_rate | 0.3514 |
| sharpe_ratio | -12.0882 |
| sortino_ratio | -5.2567 |
| max_drawdown | 0.9988 |
| cagr | -0.9311 |
| net_avg_win | 8.0783 |
| net_avg_loss | -20.3737 |
| avg_hold_time_bars | 3.4077 |
| exposure | 0.1402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
