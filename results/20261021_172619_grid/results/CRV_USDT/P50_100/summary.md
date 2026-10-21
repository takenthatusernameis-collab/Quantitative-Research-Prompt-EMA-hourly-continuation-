# EMA Hourly Continuation — CRV/USDT P50_100

**Symbol:** CRV/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7676 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9956 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5454 |
| sortino_ratio | -0.4146 |
| max_drawdown | 0.4023 |
| cagr | -0.1737 |
| net_avg_win | 71.8618 |
| net_avg_loss | -93.6152 |
| avg_hold_time_bars | 8.4514 |
| exposure | 0.1345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
