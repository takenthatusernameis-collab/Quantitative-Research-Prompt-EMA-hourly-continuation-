# EMA Hourly Continuation — ETN/USDT P26_55

**Symbol:** ETN/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 851 |
| net_profit_factor | 0.2909 |
| net_win_rate | 0.3373 |
| gross_profit_factor | 0.4787 |
| gross_win_rate | 0.3502 |
| sharpe_ratio | -12.0144 |
| sortino_ratio | -5.4155 |
| max_drawdown | 0.9972 |
| cagr | -0.9385 |
| net_avg_win | 14.2545 |
| net_avg_loss | -24.9336 |
| avg_hold_time_bars | 4.5194 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
