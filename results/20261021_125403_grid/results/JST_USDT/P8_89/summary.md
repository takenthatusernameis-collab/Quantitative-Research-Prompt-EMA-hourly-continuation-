# EMA Hourly Continuation — JST/USDT P8_89

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7444 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.1011 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -1.7468 |
| sortino_ratio | -0.5244 |
| max_drawdown | 0.4914 |
| cagr | -0.2166 |
| net_avg_win | 57.4609 |
| net_avg_loss | -85.6456 |
| avg_hold_time_bars | 32.8758 |
| exposure | 0.6590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
