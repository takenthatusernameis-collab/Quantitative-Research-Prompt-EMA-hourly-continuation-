# EMA Hourly Continuation — MOG/USDT P8_89

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.8081 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0471 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -2.1572 |
| sortino_ratio | -0.8031 |
| max_drawdown | 0.6583 |
| cagr | -0.3184 |
| net_avg_win | 76.3053 |
| net_avg_loss | -96.8237 |
| avg_hold_time_bars | 20.0831 |
| exposure | 0.6370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
