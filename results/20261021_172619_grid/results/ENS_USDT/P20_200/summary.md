# EMA Hourly Continuation — ENS/USDT P20_200

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.8535 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0247 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -0.7027 |
| sortino_ratio | -0.1572 |
| max_drawdown | 0.2356 |
| cagr | -0.0715 |
| net_avg_win | 79.9265 |
| net_avg_loss | -96.7633 |
| avg_hold_time_bars | 61.3115 |
| exposure | 0.6800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
