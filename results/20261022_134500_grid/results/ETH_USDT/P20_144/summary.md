# EMA Hourly Continuation — ETH/USDT P20_144

**Symbol:** ETH/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.4650 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8802 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -4.4265 |
| sortino_ratio | -1.2036 |
| max_drawdown | 0.7908 |
| cagr | -0.4486 |
| net_avg_win | 38.9748 |
| net_avg_loss | -71.0810 |
| avg_hold_time_bars | 35.9231 |
| exposure | 0.6156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
