# EMA Hourly Continuation — ENA/USDT P21_89

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.9220 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0771 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -0.4901 |
| sortino_ratio | -0.1524 |
| max_drawdown | 0.2925 |
| cagr | -0.0732 |
| net_avg_win | 84.4415 |
| net_avg_loss | -99.3587 |
| avg_hold_time_bars | 16.4861 |
| exposure | 0.3500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
