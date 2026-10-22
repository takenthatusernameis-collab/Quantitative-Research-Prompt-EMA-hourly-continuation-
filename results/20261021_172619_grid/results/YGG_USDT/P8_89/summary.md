# EMA Hourly Continuation — YGG/USDT P8_89

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.9118 |
| net_win_rate | 0.5190 |
| gross_profit_factor | 1.0854 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -0.7368 |
| sortino_ratio | -0.2425 |
| max_drawdown | 0.4267 |
| cagr | -0.1105 |
| net_avg_win | 96.8238 |
| net_avg_loss | -114.5837 |
| avg_hold_time_bars | 26.8764 |
| exposure | 0.6397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
